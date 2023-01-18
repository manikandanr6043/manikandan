resource "aws_instance" "foo" {
  ami           = "ami-094125af156557ca2" # us-west-2
  instance_type = var.instancetype
  tags = {
    Name = "machine1"
  }
  subnet_id            = "subnet-0601fa7dacf72dfec"
  key_name             = "mfadisable"
  iam_instance_profile = "${aws_iam_instance_profile.ec2_profile.name}"
  user_data            = file("script.sh")
}
resource "aws_instance" "foo1" {
  ami           = "ami-094125af156557ca2" # us-west-2
  instance_type = var.instancetype
  tags = {
    Name = "machine2"
  }
  subnet_id            = "subnet-0601fa7dacf72dfec"
  key_name             = "mfadisable"
  iam_instance_profile = "${aws_iam_instance_profile.ec2_profile.name}"
  user_data            = file("script.sh")
}









