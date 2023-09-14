

#Creates the DynamoDB table with the stat attribute
resource "aws_dynamodb_table" "cloud-resume-stats-test" {
  name           = "cloud-resume-stats-test"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "stat"

  attribute {
    name = "stat"
    type = "S"
  }

  tags = {
    Name        = "Dynamo-DB-Table"
    Environment = "Dev"
    }

}