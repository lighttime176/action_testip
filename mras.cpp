#include "mras.h"

void MRAS_Adaptive_Init(MRAS_Adaptive *mras, float kp, float ki, float ts,
                        float Ls, float Rs, float psi_f) {
    mras->Kp = kp;
    mras->Ki = ki;
    mras->Ts = ts;
    mras->Ls = Ls;
    mras->Rs = Rs;
    mras->psi_f = psi_f;

    mras->id_hat = 0.0f;
    mras->iq_hat = 0.0f;

    mras->est_speed = 0.0f;
    mras->est_theta = 0.0f;
    mras->error_integral = 0.0f;
}

void MRAS_Adaptive_Update(MRAS_Adaptive *mras,
                          float ud, float uq,
                          float id, float iq) {
    float L = mras->Ls;
    float R = mras->Rs;
    float Ts = mras->Ts;

    // === 可调模型 ===
    // 电流估计值微分近似：Euler法积分
    float did_hat = (-(R / L) * mras->id_hat + mras->est_speed * mras->iq_hat + ud / L);
    float diq_hat = (-mras->est_speed * mras->id_hat - (R / L) * mras->iq_hat + uq / L);

    mras->id_hat += Ts * did_hat;
    mras->iq_hat += Ts * diq_hat;

    // === 自适应律 ===
    float error = id * mras->iq_hat - mras->id_hat * iq - (mras->psi_f / L) * (iq - mras->iq_hat);

    mras->error_integral += error * Ts;

    // PI控制器更新估计转速
    mras->est_speed = mras->Kp * error + mras->Ki * mras->error_integral;

    // === 积分获得位置 ===
    mras->est_theta += mras->est_speed * Ts;

    // 保证角度在 0 ~ 2π 内
    if (mras->est_theta > 2 * 3.1415926f)
        mras->est_theta -= 2 * 3.1415926f;
    else if (mras->est_theta < 0)
        mras->est_theta += 2 * 3.1415926f;
}


#ifndef MRAS_H
#define MRAS_H

typedef struct {
    float Kp;
    float Ki;
    float Ts;       // 采样周期
    float Ls;       // 电感
    float Rs;       // 电阻
    float psi_f;    // 永磁体磁链

    double id_hat;
    double iq_hat;

    double est_speed;       // 估计转速
    double est_theta;       // 估计位置
    double error_integral;  // 误差积分项
} MRAS_Adaptive;

// 初始化函数
void MRAS_Adaptive_Init(MRAS_Adaptive *mras, float kp, float ki, float ts,
                        float Ls, float Rs, float psi_f);

// 每个控制周期调用一次，输入当前 ud, uq, id, iq
void MRAS_Adaptive_Update(MRAS_Adaptive *mras,
                          float ud, float uq,
                          float id, float iq);

#endif
