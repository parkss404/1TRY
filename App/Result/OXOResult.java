package com.example.a1try.result;

import android.os.Bundle;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class OXOResult extends AppCompatActivity {

    private Button btn_121;
    
    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result121);
        
        TextView OXO=findViewById(R.id.OXO);
        
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
    }
}
