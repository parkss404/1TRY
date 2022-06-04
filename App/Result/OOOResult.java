package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class OOOResult extends AppCompatActivity {

    private Button btn_111;
    
    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result111);
        
        TextView OOO=findViewById(R.id.OOO);
        btn_111=findViewById(R.id.btn_111);
        
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
    }
}
