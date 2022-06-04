package com.example.a1try.result;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.MainActivity;
import com.example.a1try.R;

import java.util.Random;

public class OXOResult extends AppCompatActivity {

    private Button btn_121;
    private Button btn_end3;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result121);

        TextView OXO=findViewById(R.id.OXO);
        btn_121=findViewById(R.id.btn_121);
        btn_end3=findViewById(R.id.btn_end3);

        String[] OXOtxt=getResources().getStringArray(R.array.OXOtxt);
        Random random=new Random();
        int n= random.nextInt(OXOtxt.length-1);

        OXO.setText(OXOtxt[n]);

        btn_121.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] OXOtxt=getResources().getStringArray(R.array.OXOtxt);
                Random random=new Random();
                int n= random.nextInt(OXOtxt.length);

                OXO.setText(OXOtxt[n]);
            }
        });

        btn_end3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(OXOResult.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}
