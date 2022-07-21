# aws_rotate_iam_access_keys

Usage:

Install required modules
```
pip install -r requirements.txt
```

Get list of aws profiles configured on local machine:
```
./list_profiles.py
```

I use aws profile `mfa` to get aws sts token. Then I put sts token to AWS profile `default`

Get sts token.
```
./get_token_using_mfa.py
```

Get list of IAM access keys
```
./list_access_keys.py
```

Create new access key
```
./create_access_key.py
```

Delete access key
```
./delete_access_key.py
```
