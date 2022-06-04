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

public class XOOResult extends AppCompatActivity {

    private Button btn211;
    private Button btn_end5;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result211);

        TextView XOO=findViewById(R.id.XOO);
        btn211=findViewById(R.id.btn_211);
        btn_end5=findViewById(R.id.btn_end5);

        String[] XOOtxt=getResources().getStringArray(R.array.XOOtxt);
        Random random=new Random();
        int n= random.nextInt(XOOtxt.length-1);

        XOO.setText(XOOtxt[n]);

        btn211.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] XOOtxt=getResources().getStringArray(R.array.XOOtxt);
                Random random=new Random();
                int n= random.nextInt(XOOtxt.length);

                XOO.setText(XOOtxt[n]);
            }
        });

        btn_end5.setOnClickListener(new View.OnClickListener(){
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
                                moveTaskToBack(true);
                                finishAndRemoveTask();
                                System.exit(0);
                            }
                        });
                AlertDialog alert=builder.create();
                alert.setTitle("종료 알림창");
                alert.show();
            }   
        });
    }
}
