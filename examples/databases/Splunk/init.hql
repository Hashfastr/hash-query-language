database('splunk')
| where index =~ "*"
| take 10
| where field2 matches regex @"test.*test"
