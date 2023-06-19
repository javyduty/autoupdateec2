#!/usr/bin/env python # [1]
"""
This script automatically updates ec2 instances on aws 
by connecting to them and passing in commands

Usage: update.py IP_ADDRESS PEM_FILE_NAME
"""
import os
import sys
import paramiko


# Pass in information about the EC2 intances that you want to update.
def update_instance(remote_ip, pem_key_name):
    instance_key = PATH + pem_key_name
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname="127.0.0.1", username="ec2-user", pkey=paramiko.RSAKey.from_private_key_file(instance_key), port=1000)
    update_command = "sudo yum update -y"
    stdin, stdout, stderr = client.exec_command(update_command)
    exit_status = stdout.channel.recvd_exit_status()
    if exit_status == 0:
        print("Updated successfully!")
    else:
        print("Unexpected error while updating")
    client.close()

def parameter_check():
    remote_ip = sys.argv[0]
    pem_key_name = sys.argv[1]

    if not remote_ip or not pem_key_name:
        print("Invalid parameters passed")
        system.exit(0)

    update_instance(remote_ip, pem_key_name)

PATH = os.getenv("HOME").replace("\\", "/")
