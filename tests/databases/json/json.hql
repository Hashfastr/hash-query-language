database('json').http('https://files.hashfastr.com/hql-datasets/big.json')
| take 1
| count as _counts