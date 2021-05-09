package com.hq.engineerman123;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

@SuppressLint("SetTextI18n")
public class MainActivity extends AppCompatActivity {

    EditText number1;
    EditText number2;
    Button calculate;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        number1 = findViewById(R.id.number1);
        number2 = findViewById(R.id.number2);
        calculate = findViewById(R.id.calculate);
        result = findViewById(R.id.result);

        calculate.setOnClickListener(view -> {
            int n1 = Integer.parseInt(number1.getText().toString());
            int n2 = Integer.parseInt(number2.getText().toString());
            int sum = n1 + n2;

            result.setText(Integer.toString(sum));
        });
    }

}