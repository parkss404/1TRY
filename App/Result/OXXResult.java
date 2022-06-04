package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class OXXResult extends AppCompatActivity {
    
    private Button btn_122;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result122);
        
        TextView OXX=findViewById(R.id.OXX);
        
        String[] OXXtxt=getResources().getStringArray(R.array.OXXtxt);
                Random random=new Random();
                int n= random.nextInt(OXXtxt.length);

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
    }
}
