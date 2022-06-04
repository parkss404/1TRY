package com.example.a1try.result;

import android.os.Bundle;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XOXResult extends AppCompatActivity {
    
    private Button btn_212;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result212);
        
        TextView XOX=findViewById(R.id.XOX);
        
        String[] XOXtxt=getResources().getStringArray(R.array.XOXtxt);
            Random random=new Random();
            int n= random.nextInt(XOXtxt.length-1);

            XOX.setText(XOXtxt[n]);
        
            btn_212.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    String[] XOXtxt=getResources().getStringArray(R.array.XOXtxt);
                    Random random=new Random();
                    int n= random.nextInt(XOXtxt.length);

                    XOX.setText(XOXtxt[n]);
                }
            });
        
    }
}
