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
    
public class XOXResult extends AppCompatActivity {

    private Button btn_212;
    private Button btn_end6;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result212);

        TextView XOX = findViewById(R.id.XOX);
        btn_212 = findViewById(R.id.btn_212);
        btn_end6 = findViewById(R.id.btn_end6);
        
        String[] XOXtxt = getResources().getStringArray(R.array.XOXtxt);
        Random random = new Random();
        int n = random.nextInt(XOXtxt.length - 1);
        
        XOX.setText(XOXtxt[n]);
        
        btn_212.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] XOXtxt = getResources().getStringArray(R.array.XOXtxt);
                Random random = new Random();
                int n = random.nextInt(XOXtxt.length);

                XOX.setText(XOXtxt[n]);
            }
        });

        btn_end6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder=new AlertDialog.Builder(OOOResult.this);
                builder.setMessage("메인으로 돌아가시겠습니까?");
                builder.setTitle("종료 알림창")
                        .setCancelable(false)
                        .setNegativeButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int main) {
                                Intent intent=new Intent(OOOResult.this,MainActivity.class);
                                startActivity(intent);
                            }
                        })
                        .setPositiveButton("No", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int end) {
                                finish();
                            }
                        });
                AlertDialog alert=builder.create();
                alert.setTitle("종료 알림창");
                alert.show();
            }
        });
    }
}
