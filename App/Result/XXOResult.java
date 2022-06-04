package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XXOResult extends AppCompatActivity {
    
    private Button btn_221;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result221);
        
        TextView XXO=findViewById(R.id.XXO);
        btn_221=findViewById(R.id.btn_221);
        
        String[] XXOtxt=getResources().getStringArray(R.array.XXOtxt);
        Random random=new Random();
        int n= random.nextInt(XXOtxt.length-1);

        XXO.setText(XXOtxt[n]);
        
        btn_221.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] XXOtxt=getResources().getStringArray(R.array.XXOtxt);
                Random random=new Random();
                int n= random.nextInt(XXOtxt.length);

                XXO.setText(XXOtxt[n]);
            }
        });
    }
}
