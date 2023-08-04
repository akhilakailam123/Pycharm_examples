output "end_point" {
  value = "${aws_api_gateway_stage.example.invoke_url}/${var.api_endpoint}?amount=100&fromCurrency=USD&toCurrency=CAD"
}