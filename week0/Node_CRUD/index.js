const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser')
const ejs = require('ejs');
const http = require('http');
const app = express();


// var connection = mysql.createConnection({ 
//     host: 'localhost',
//     user: 'root',
//     password: '',
//     database: 'employee'
// });

// connection.connect(function(error){
//     if(!!error)
//         console.log(error)
//     else
//         console.log("DB connection success");
// })

// app.set('views', path.join(__dirname, views));

// //Set Engine
// app.set('view engine', 'ejs');
// app.use(bodyParser.json());










// app.get('/', (req, res) => {
//     res.send("HEllO"); 
// })



// app.listen(3000, ()=> {
//     console.log("Express server running!");
// });



app.use(bodyParser.json());


var mysqlConnection = mysql.createConnection({ 
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'employee'
});


mysqlConnection.connect((err)=>{
    if(!err)
        console.log("DB Connection success!")
    else
        console.log("Failed" + JSON.stringify(err, undefined, 2));
});


mysqlConnection.query('SELECT * from emp', (err, res)=>{
    return console.log(res)
})

app.listen(3000, ()=> {
    console.log("Express server running!");
});

app.get('/employees',(req,res)=>{
    mysqlConnection.query('SELECT * from emp', (err, rows, fields)=>{
        if(!err)
            res.send(rows);
        else
            console.log(err);
    })

});


app.get('/employees/:id',(req,res)=>{
    mysqlConnection.query('SELECT * from emp where id=?',[req.params.id], (err, rows, fields)=>{
        if(!err)
            res.send(rows);
        else
            console.log(err);
    })

});


app.delete('/employees/:id',(req,res)=>{
    mysqlConnection.query('DELETE from emp where id=?',[req.params.id], (err, rows, fields)=>{
        if(!err)
            res.send("Employee Deleted successfully!");
        else
            console.log(err);
    })

});

app.post('/employees',(req,res)=>{
    let e = req.body;
    mysqlConnection.query('INSERT INTO emp (name, empcode, salary) VALUES(?,?,?)',[e.name, e.empcode, e.salary], (err, rows, fields)=>{
        if(!err)
            res.send("Employee added successfully!");
        else
            console.log(err);
    })

});


app.put('/employees',(req,res)=>{
    let e = req.body;
    mysqlConnection.query('UPDATE emp  set name = ?, empcode = ?, salary = ? WHERE id = ?',[e.name, e.empcode, e.salary, e.id], (err, rows, fields)=>{
        if(!err)
            res.send("Employee updated successfully!");
        else
            console.log(err);
    })

});
