var express = require('express');
var router = express.Router();
const spawn = require("child_process").spawn;
const fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
    const json = JSON.parse(fs.readFileSync('ratings.json', 'utf8'));
    return res.json(json).sendStatus(200);
    const pythonProcess = spawn('python', ["cnbc-parse.py"]);
    pythonProcess.on('exit', (code) => {
        const json = JSON.parse(fs.readFileSync('results.json', 'utf8'));
        return res.json(json).sendStatus(200);
    });
});

router.get('/data', function(req, res, next) {
    const json = JSON.parse(fs.readFileSync('output.json', 'utf8'));
    return res.json(json).sendStatus(200);
});

router.get('/ratings', function(req, res, next) {
    const json = JSON.parse(fs.readFileSync('ratings.json', 'utf8'));
    return res.json(json).sendStatus(200);
});

module.exports = router;
