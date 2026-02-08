package com.calc;

import javax.jws.WebService;

@WebService(endpointInterface = "com.calc.CalculatorPortType")
public class Calculator implements CalculatorPortType {
    public int add(int num1, int num2) {
        return num1 + num2;
    }
}