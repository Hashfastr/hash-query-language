database('splunk')
| where index =~ '''
Super code
test
'''
| take 10
| where field2 matches regex @"test.*\ntest"
