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

public class XXOResult extends AppCompatActivity {

    private Button btn_221;
    private Button btn_end7;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result221);

        TextView XXO=findViewById(R.id.XXO);
        btn_221=findViewById(R.id.btn_221);
        btn_end7=findViewById(R.id.btn_end7);

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

        btn_end7.setOnClickListener(new View.OnClickListener(){
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
