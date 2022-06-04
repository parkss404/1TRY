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
import com.example.a1try.question3.Question3OO;

import java.util.Random;

public class OOXResult extends AppCompatActivity {

    private Button btn_112;
    private Button btn_end2;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result112);

        TextView OOX=findViewById(R.id.OOX);
        btn_112=findViewById(R.id.btn_112);
        btn_end2=findViewById(R.id.btn_end2);

        String[] OOXtxt=getResources().getStringArray(R.array.OOXtxt);
        Random random=new Random();
        int n= random.nextInt(OOXtxt.length-1);

        OOX.setText(OOXtxt[n]);

        btn_112.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                String[] OOXtxt=getResources().getStringArray(R.array.OOXtxt);
                Random random=new Random();
                int n= random.nextInt(OOXtxt.length);

                OOX.setText(OOXtxt[n]);
            }
        });

        btn_end2.setOnClickListener(new View.OnClickListener(){
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
