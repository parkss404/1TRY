package com.example.a1try;

import androidx.appcompat.app.AppCompatActivity;

import java.net.URL;

public class MainActivity extends AppCompatActivity {

    private Button btn_f;
  
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_f=findViewById(R.id.btn_f);

        btn_f.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(MainActivity.this,Question1.class);
                startActivity(intent);
            }
        });
    }
}
