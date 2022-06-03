package com.example.a1try.question3;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.result.OOOResult;
import com.example.a1try.R;
import com.example.a1try.result.OOXResult;

public class Question3OO extends AppCompatActivity {

    private Button btn_5;
    private Button btn_6;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question311);

        btn_5=findViewById(R.id.btn_5);
        btn_6=findViewById(R.id.btn_6);

        btn_5.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3OO.this, OOOResult.class);
                startActivity(intent);
            }
        });

        btn_6.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3OO.this, OOXResult.class);
                startActivity(intent);
            }
        });
    }
}
