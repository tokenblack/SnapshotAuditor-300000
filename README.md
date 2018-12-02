<<<<<<< HEAD
# SnapshotAuditor-300000

=======
# snapshot-auditor-30k
>>>>>>> 013bbba7177cb26f73cc5b8953e967b8c8010138
Demo project to manage AWS EC2 instance snapshots.

## About

This is a demo project, and it uses Boto3 to manage AWS EC2 instance snapshots.

## Configuring

tokenblack uses the configuration file created by the AWS CLI. For example:

`aws configure --profile tokenblack`

## Running

`pipenv run python scripts/ls_instances.py <command> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* depends on command
*project* is optional
