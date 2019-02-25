package com.example.miguelfrias.natalyproject;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Switch;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SensorManager sManager;
        Sensor acelerometro;

        TextView lblLuces;
        TextView lbl;
        TextView lblEstado;

        Switch swtPosteriores;
        Switch swtTraseras;

        String json2Send;

        float xAcc;
        float yAcc;
        float zAcc;

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        sManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        acelerometro = sManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sManager.registerListener(leerDatos,acelerometro,sManager.SENSOR_DELAY_FASTEST);

        xAcc = 0;
        yAcc= 0;
        zAcc = 0;
        json2Send = "";
        lbl = findViewById(R.id.lbl);
        lblLuces = findViewById(R.id.lblLuces);
        lblEstado = findViewById(R.id.lblEstado);

        swtPosteriores = findViewById(R.id.swtPosteriores);
        swtTraseras = findViewById(R.id.swtTraseras);


    }

    public SensorEventListener leerDatos = new SensorEventListener() {
        @Override
        public void onSensorChanged(SensorEvent event) {
            float xAcc =
        }

        @Override
        public void onAccuracyChanged(Sensor sensor, int accuracy) {

        }
    }
}
