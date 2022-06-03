package com.example.a1try.question1;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.content.Intent;
import android.widget.Button;
import android.view.View;

import com.example.a1try.question2.Question2;
import com.example.a1try.R;

public class Question1 extends AppCompatActivity {

    private Button btn_1;
    private Button btn_2;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState){
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question1);

        btn_1=findViewById(R.id.btn_1);
        btn_2=findViewById(R.id.btn_2);

        btn_1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question1.this, Question2.class);
                startActivity(intent);
            }
    }
}
