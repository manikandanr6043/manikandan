curl -s https://cis-infosec-cdn.trimble.com/crowdstrike/trimble-cis-falcon-installer.sh | sudo bash
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo systemctl status amazon-ssm-agent
sudo systemctl start amazon-ssm-agent