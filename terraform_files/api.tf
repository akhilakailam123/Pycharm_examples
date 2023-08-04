resource "aws_instance" "for_credentials" {
  ami           = "ami-0f34c5ae932e6f0e4"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld"
    owner = "aws_client"
  }
}
