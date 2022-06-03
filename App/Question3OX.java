package com.example.a1try.question3;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.result.OXOResult;
import com.example.a1try.R;
import com.example.a1try.result.OXXResult;

public class Question3OX extends AppCompatActivity {

    private Button btn_7;
    private Button btn_8;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_question312);

        btn_7=findViewById(R.id.btn_7);
        btn_8=findViewById(R.id.btn_8);

        btn_7.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3OX.this, OXOResult.class);
                startActivity(intent);
            }
        });

        btn_8.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(Question3OX.this, OXXResult.class);
                startActivity(intent);
            }
        });
    }
}
