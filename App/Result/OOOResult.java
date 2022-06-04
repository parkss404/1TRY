package com.example.a1try.result;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.MainActivity;
import com.example.a1try.R;
import com.example.a1try.question3.Question3OO;

import java.util.Random;

public class OOOResult extends AppCompatActivity {

    private Button btn_111;
    private Button btn_end1;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result111);

        TextView OOO=findViewById(R.id.OOO);
        btn_111=findViewById(R.id.btn_111);
        btn_end1=findViewById(R.id.btn_end1);

        String[] OOOtxt=getResources().getStringArray(R.array.OOOtxt);
        Random random=new Random();
        int n= random.nextInt(OOOtxt.length-1);

        OOO.setText(OOOtxt[n]);

        btn_111.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                String[] OOOtxt = getResources().getStringArray(R.array.OOOtxt);
                Random random = new Random();
                int n = random.nextInt(OOOtxt.length);

                OOO.setText(OOOtxt[n]);
            }
        });

        btn_end1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(OOOResult.this, MainActivity.class);
                startActivity(intent);
            }
        });

    }
}
