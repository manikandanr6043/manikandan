resource "aws_iam_role_policy" "ssm_policy" {
  name   = "ssm_policy"
  role   = aws_iam_role.ec2_assume.id
  policy = file("ssm_policy.json")
}
resource "aws_iam_role" "ec2_assume" {
  name               = "ec2_assume"
  assume_role_policy = file("ec2_assume.json")
}
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2_profile"
  role = "${aws_iam_role.ec2_assume.name}"
}
