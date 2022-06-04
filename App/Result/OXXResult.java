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

import java.util.Random;

public class OXXResult extends AppCompatActivity {

    private Button btn_122;
    private Button btn_end4;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result122);

        TextView OXX=findViewById(R.id.OXX);
        btn_122=findViewById(R.id.btn_122);
        btn_end4=findViewById(R.id.btn_end4);

        String[] OXXtxt=getResources().getStringArray(R.array.OXXtxt);
        Random random=new Random();
        int n= random.nextInt(OXXtxt.length-1);

        OXX.setText(OXXtxt[n]);

        btn_122.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    String[] OXXtxt=getResources().getStringArray(R.array.OXXtxt);
                    Random random=new Random();
                    int n= random.nextInt(OXXtxt.length);

                    OXX.setText(OXXtxt[n]);
            }
        });

        btn_end4.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(OXXResult.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}
