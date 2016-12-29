var sherdog = require('sherdog')
var url = "http://www.sherdog.com/fighter/Amanda-Nunes-31496"
sherdog.getFighter(url, function(data) {
	/*for (i=0;i<data.fights.length;i++) {
    	console.log(data.fights[i].method);
	}*/
	console.log(data)
  });