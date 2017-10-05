# Slack_File-Delete
This pythons program is for delete in "Slack"s storage files"

## Environment setting
Insert your setting to "Setting.json"
Setting.json is written by amaing this format
```json
{
	"token":"__ Your_token __",
	"domain":"__ Your_teem_domain __",
	"User":[
		{
			"name":"__USER_ID__",
			"admin":"false"
		}
	],
	"Day":"__DAYS__",
	"Ignore":[
		{
			"Posts":"true",
			"Snippets":"true",
			"Image":"true",
			"Google_docs":"true",
			"Zip":"true",
			"PDF":"true"
		}
	]
}
```

# Get Slack token
Please found Your Slack User ID in https://api.slack.com/methods/users.list
Please taken Your Slack Token in https://api.slack.com/custom-integrations/legacy-tokens
