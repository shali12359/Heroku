from flask import Flask, request, jsonify

def sayHello(name):
  return 'Hello ' + name

def sayAge(age):
  return 'I am ' + age