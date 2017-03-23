# minecraft-status

Python app for getting Minecraft server status.

This project is forked off of the barebones Python app using django provided by Heroku.
*[Source readme](https://github.com/heroku/python-getting-started/blob/master/README.md)

This project makes use of Dinnerbone's MC Status API found [here](https://github.com/Dinnerbone/mcstatus.git) and packages the results into JSON that can be used on whatever webpage is desired to display the server status.

## Sample usage
```javascript
url = ''; // TODO - your Python app's URL here
$.getJSON(url + "?callback=?",
	function(data) {
		var output = "";
		var isOnline = false;
		if (!data) {
			output = "The server is down.";
			return;
		} else {		
			isOnline = true;
			output = 'Players online: ' + data.playerCount + " / " + data.maxPlayers + "<br/>";
			
			if (data.playerNames.length > 0) {
				output += ('&nbsp;&nbsp;&nbsp;' + data.playerNames.join(", ") + "<br/>");
			}
			output += ("Version: " + data.version + "<br/>Map Name: " + data.map + "<br/>");
		}
		// TODO - Stop any loading animations here, append your output to some div on your web page
		$('#status').append(output);
});
```
