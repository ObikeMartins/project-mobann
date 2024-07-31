




# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Define an EC2 instance
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # ubuntu
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleInstance"
  }
}

