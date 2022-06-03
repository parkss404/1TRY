package com.example.a1try.question3;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.result.XOOResult;
import com.example.a1try.R;
import com.example.a1try.result.XOXResult;

public class Question3XO extends AppCompatActivity {

    private Button btn_9;
    private Button btn_10;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question321);

        btn_9=findViewById(R.id.btn_9);
        btn_10=findViewById(R.id.btn_10);

        btn_9.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3XO.this, XOOResult.class);
                startActivity(intent);
            }
        });

        btn_10.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3XO.this, XOXResult.class);
                startActivity(intent);
            }
        });
    }
}
