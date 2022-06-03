package com.example.a1try.question3;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

import com.example.a1try.result.XXOResult;
import com.example.a1try.result.XXXResult;

public class Question3XX extends AppCompatActivity {

    private Button btn_11;
    private Button btn_12;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question322);

        btn_11=findViewById(R.id.btn_11);
        btn_12=findViewById(R.id.btn_12);

        btn_11.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3XX.this, XXOResult.class);
                startActivity(intent);
            }
        });

        btn_12.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3XX.this, XXXResult.class);
                startActivity(intent);
            }
        });
    }
}
