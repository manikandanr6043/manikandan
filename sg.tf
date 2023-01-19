resource "aws_security_group" "allow_tls1" {
  name        = "allow_tls1"
  description = "Allow TLS inbound traffic"
  vpc_id      = "vpc-0350118ca58f04635"
}