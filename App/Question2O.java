package com.example.a1try.question2;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.content.Intent;
import android.widget.Button;
import android.view.View;

import com.example.a1try.question3.Question3OO;
import com.example.a1try.question3.Question3OX;
import com.example.a1try.R;

public class Question2O extends AppCompatActivity {

    private Button btn_3;
    private Button btn_4;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState){
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question21);

        btn_3=findViewById(R.id.btn_3);
        btn_4=findViewById(R.id.btn_4);

        btn_3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question2O.this, Question3OO.class);
                startActivity(intent);
            }
        });

        btn_4.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question2O.this, Question3OX.class);
                startActivity(intent);
            }
        });
    }
}
