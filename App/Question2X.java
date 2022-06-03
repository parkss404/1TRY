package com.example.a1try.question2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.question3.Question3XO;
import com.example.a1try.question3.Question3XX;
import com.example.a1try.R;

public class Question2X extends AppCompatActivity {

    private Button btn_3;
    private Button btn_4;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState){
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question22);

        btn_3=findViewById(R.id.btn_3);
        btn_4=findViewById(R.id.btn_4);

        btn_3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question2X.this, Question3XO.class);
                startActivity(intent);
            }
        });

        btn_4.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question2X.this, Question3XX.class);
                startActivity(intent);
            }
        });
    }
}
