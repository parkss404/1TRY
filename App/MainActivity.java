package com.example.a1try;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.content.Intent;
import android.widget.Button;
import android.view.View;

import java.net.URL;

public class MainActivity extends AppCompatActivity {

    private Button btn_f;
    private Button btn_1link;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_f=findViewById(R.id.btn_f);
        btn_1link=findViewById(R.id.btn_1link);

        btn_f.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(MainActivity.this,Question1.class);
                startActivity(intent);
            }
        });

        btn_1link.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(Intent.ACTION_VIEW);
                intent.setData(URL.("http://pf.kakao.com/_vgheb");));
                startActivity(intent);
            }
        });
    }
}
