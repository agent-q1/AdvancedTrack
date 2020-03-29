const express=require('express');
const exphbs =require('express-handlebars');
const fs = require('fs');
const app=express();


var str='sample';
var resultCalculated = false;

//Handlebars Middleware
app.engine('handlebars',exphbs({
    defaultLayout: 'main'
}));
app.use(express.static('views/images'));  
app.set('view engine','handlebars');

//Index route
app.get('/',(req,res)=>{
    const title ='WELCOME TO AUTOGRADING';
    res.render('index',{
        title: title
    });
});

//About route
app.get('/about',(req,res)=>{
    res.render('about');
});

//Select route
app.get('/select',function(req,res){
    res.render('select');
})
app.get('/process_get_name',function(req,res){
    str=req.query.image_name;
    res.render('displaySample',{
       image : str
    });
})
//Sample coordinate submit

app.get('/process_get',function(req,res){
   
    var substr = str.split('.');

    fs.writeFile(substr[0]+'.txt',req.query.coordinates,function(err){
        if(err)
            throw err;
            console.log('updated');
    })
    res.render('updateCoordinates',{
        image : substr[0]
    });
})

//Setting answer key
app.get('/answerKey',function(req,res){
    res.render('answerKey');
})

//
app.get('/process_get_answer', function(req,res){
    var ans = req.query.answer;
    var substr = str.split('.');
    fs.writeFile(substr[0]+'answer.txt', req.query.answer,function(err){
        if(err)
            throw err;
            console.log('updated answer key');
    });
    fs.writeFile('request1.txt',substr[0],function(err)
    {
        
        if(err)
        throw err;
        console.log('request1');
    });
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["./final.py"] );
    res.render('answerKeyUpdated');


})


app.get('/student',function(req,res){
    res.render('studentPaper');
})

app.get('/process_get_student', function(req,res){

    var stud = req.query.roll_no;
    fs.writeFile('request.txt', req.query.exam_type + ' ' + req.query.roll_no,function(err){
        if(err)
            throw err;
        console.log('student grading request accepted');
    })
   
    res.render('studentRequest');
})

//Route for result viewing
var typeExam,rollNo;
app.get('/results',function(req,res){
    
     fs.readFile('request.txt','utf8',function read(err,data){
            if(err)
            throw(err);
            
            
            var each = data.split(' ');
                    typeExam = each[0];
                    rollNo = each[1]
                // console.log(typeExam);
                    
                
                fs.readFile(typeExam+'result.txt','utf8',function read(err,data){
                    if(err)
                        throw(err);
                    var each = data.split('\n');
                   
                    
                    //console.log(each);
                    for(var x = 0;x<each.length-1;x++)
                    {
                        
                        
                        var eachRow = each[x];
                        RollSplit = eachRow.split(' ');
                        eachRollNo = RollSplit[0];
                        eachRollMarks = RollSplit[1];
                        totalMarks = RollSplit[2];
                        GivenAnswer = RollSplit[3];
                        RightAnswer=RollSplit[4];
                        
                        if(eachRollNo==rollNo)
                            { 
                              res.render('results',{
                                 marks1:eachRollMarks,
                                 marks2:totalMarks,
                                 givenAnswer:GivenAnswer,
                                 ReqAnswer:RightAnswer
                            })              
                                                     
                            }

                        
                        
            
                    }
          
      
    });


    });
    

})
const port= 5000;

app.listen(port,() =>{
    console.log(`Server started on port ${port}`);
});