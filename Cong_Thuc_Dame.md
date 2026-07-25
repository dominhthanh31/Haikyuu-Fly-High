# Công Thức Tính Sát Thương (Dame)

> [!WARNING]
> # ⚠️⚠️⚠️ CHÚ Ý QUAN TRỌNG ⚠️⚠️⚠️
>
> ## TẤT CẢ NỘI DUNG TRONG FILE NÀY CHỈ LÀ TÀI LIỆU THAM KHẢO
>
> ---
>
> Công thức và số liệu được **dịch từ tài liệu cộng đồng**, chưa được kiểm chứng chính thức bởi nhà phát hành.
>
> - Có thể có **sai sót** trong quá trình dịch hoặc phân tích ngược
> - Công thức có thể **thay đổi theo phiên bản game** mà không có thông báo
> - Một số cơ chế có thể hoạt động **khác với mô tả** trong tài liệu này
>
> **Không nên áp dụng một cách tuyệt đối. Hãy luôn kiểm chứng bằng thực tế khi có thể.**
>
> ---

> Nguồn: (https://m.gamer.com.tw/forum/C.php?bsn=79433&snA=657&bpage=1&ltype=)
> Nguồn: (https://m.gamer.com.tw/forum/C.php?bsn=79433&page=&snA=49&last=)
> Nguồn: (https://docs.google.com/document/d/1GV8TH20AmfEvi-bsQSzXW3VXWAhASY6JuM1sYTN3-IA/edit?tab=t.0)

---

## I. TỔNG QUAN

### 12 Cơ chế ảnh hưởng dame
Thuộc tính · Bùng nổ · Kỹ thuật · Sức mạnh kỹ năng · Khắc chế · Sĩ khí · BNP · Thể lực · Thay người · Buff/Debuff · CD kỹ năng · Nhân đôi

Tuy có 12 cơ chế, nhưng quy về **6 vùng nhân** (乘區):

| Vùng nhân | Tên Việt | Ghi chú |
|---|---|---|
| 屬性區 | **Vùng Chỉ số** | Phức tạp nhất |
| 超常發揮區 | **Vùng Bùng nổ** | Crit rate × crit damage |
| 技巧區 | **Vùng Kỹ thuật** | [KT tấn công]/[KT phòng thủ] |
| 威力區 | **Vùng Sức mạnh kỹ năng** | Bội số kỹ năng + bonus |
| BNP常數 | **Hằng số BNP** | Chỉ ảnh hưởng giao bóng |
| 加倍常數 | **Hằng số Nhân đôi** | ×1/×2/×3 ngẫu nhiên |

Khắc chế → thuộc Vùng Sức mạnh kỹ năng. Sĩ khí → thuộc Vùng Chỉ số. CD kỹ năng → thuộc Vùng Sức mạnh kỹ năng.

---

## II. CÔNG THỨC

### Công thức tổng quát
```
Dame = Vùng_CS × Vùng_BN × Vùng_KT × Vùng_SM × Hằng_BNP × Hằng_Nhân
```

### Công thức chi tiết
```
Dame kỳ vọng =
  ([CS_gốc × (1 + % bonus_gốc) + điểm_cố_định] × (1 + % bonus_thường) + CS_gốc × % kizuna_trường)
  × (1 + [Ý thức]/[Phản xạ] × [Sức mạnh]/[Tinh thần])
  × (1 + [KT tấn công]/[KT phòng thủ])
  × Sức_mạnh_kỹ_năng
  × Hằng_BNP
  × Hằng_Nhân
```

---

## III. SÁU VÙNG NHÂN — CHI TIẾT

---

### 1. Vùng Chỉ số (屬性區)

Đây là vùng phức tạp nhất. Có **3 loại bonus chỉ số** hoạt động khác nhau:

#### Loại 1 — Bonus chỉ số gốc (基礎屬性加成)
> Hiển thị dưới dạng **chữ xanh** trên panel nhân vật.

Bao gồm:
- Training (huấn luyện)
- Kizuna nhân vật (角色羈絆)
- Tiềm năng — Potential (潛能)
- Cộng hưởng 4, 8, 12
- Ứng viên — Support (應援) ← **KHÔNG hiện trên panel**

#### Loại 2 — Bonus chỉ số thông thường (屬性加成)
> Áp dụng lên toàn bộ chỉ số sau khi đã cộng Loại 1.

Bao gồm:
- Kỹ năng nhân vật (角色技能)
- Memory skill (追憶技能)
- Cộng hưởng 6, 10
- Sĩ khí (士氣) — trạng thái bùng phát
- Thể lực (體力) — giảm chỉ số khi thấp

#### Loại 3 — Bonus chỉ số cố định (固定屬性加成)
> Cộng thêm vào sau Loại 2, không bị ảnh hưởng bởi Loại 2.

Bao gồm:
- Kizuna trường học dạng **cộng điểm % chỉ số gốc** (屬性加成類學校羈絆)

#### Công thức Vùng Chỉ số
```
CS = [CS_gốc × (1 + % Loại1) + điểm_cố_định_Loại1] × (1 + % Loại2) + CS_gốc × % Kizuna_trường
```

> **Lưu ý thực tế:** Cách nhanh nhất để lấy tổng chỉ số là xem con số trên panel 6 chiều (chữ xanh tổng) **cộng thêm giá trị ứng viên** (vì ứng viên không tính vào chữ xanh).

---

### 2. Vùng Bùng nổ / Nice Play (超常發揮區)

| Chỉ số | Tên Việt | Giá trị gốc (ẩn) | Hiển thị trên panel |
|---|---|---|---|
| 意識 / 反應 | [Ý thức] / [Phản xạ] | 5% | Có |
| 力量 / 精神 | [Sức mạnh] / [Tinh thần] | **50%** | **Không** |

- **Không Nice Play:** × 1
- **Nice Play:** × (150% + [Sức mạnh]/[Tinh thần] tích lũy)
- **Dame kỳ vọng (tính xác suất):**
  ```
  × [1 + (5% + [Ý thức]) × (50% + [Sức mạnh])]
  ```

> Ví dụ: [Ý thức] = 149%, [Sức mạnh] = 249.5%
> → Kỳ vọng = 1 + 1.54 × 2.995 ≈ ×3.495
> → Dame Nice Play thực tế = ×(1.5 + 2.495) = ×3.995

---

### 3. Vùng Kỹ thuật (技巧區)

Cộng **tất cả** % [Kỹ thuật tấn công] hoặc [Kỹ thuật phòng thủ]:
```
Vùng_KT = 1 + tổng % [KT tấn công/phòng thủ]
```

> Ví dụ: KT tấn công 40% → Vùng_KT = 1.4

---

### 4. Vùng Sức mạnh kỹ năng (威力區)

```
Vùng_SM = bội_số_kỹ_năng + % tăng_sức_mạnh + % khắc_chế
```

- **Bội số kỹ năng:** con số × trong mô tả kỹ năng (VD: × 260%)
- **% tăng sức mạnh:** các buff cộng thêm vào bội số kỹ năng đó
- **Khắc chế đội hình:** +30% nếu loại hành động khắc chế đối thủ

**Trường hợp đặc biệt — CD kỹ năng:**
Khi kỹ năng hết CD nhưng chưa sẵn sàng vẫn có thể thực hiện → bội số = **100%** (tức là đòn thường).

> Ví dụ: Kỹ năng 389% + bonus 0% + không khắc chế → Vùng_SM = 3.89

---

### 5. Hằng số BNP (BNP常數)

**Chỉ áp dụng cho giao bóng (服務):**

| Kết quả giao bóng | Hệ số |
|---|---|
| Bad (B) | × 0.8 |
| Normal (N) | × 1.0 |
| Perfect (P) | × 1.2 |

Tất cả hành động khác (đập, tốc công, đỡ, chắn, cứu, chuyền): **× 1**

---

### 6. Hằng số Nhân đôi (加倍常數)

Hệ thống ẩn, không được giải thích trong game. Mỗi lần chạm bóng có thể ngẫu nhiên cho ra:
- **× 1** (thường)
- **× 2** (phổ biến với đập mạnh/tốc công)
- **× 3** (hiếm)

> Xác suất và loại nhân đôi khả dụng khác nhau tùy hành động. **Đập mạnh/tốc công mặc định tính × 2** vì đa số trường hợp đều ra × 2.

---

## IV. VÍ DỤ TÍNH DAME

### Ví dụ 1 — Tính Vùng Chỉ số (Hinata trong đội Karasuno, sĩ khí bùng phát)

**Thông tin:**
- CS gốc [Tốc công]: 1475
- Training: +6.5% + 220 điểm
- Kizuna nhân vật: +5%
- Cộng hưởng: +15%×2 (= +30%)
- Tiềm năng: +10%×3 (= +30%) + 300 điểm cố định
- Phụ từ điều tiềm năng: +24 điểm
- Memory (追憶): +663 điểm
- Ứng viên (Support): +200 điểm
- Sĩ khí bùng phát: +20% (tức × 1.2 → 1+20% = bonus 20%)
- Kizuna trường Karasuno: +10% CS gốc (loại Loại 3)

**Tính:**
```
CS = [1475 × (1 + 6.5% + 5% + 15%×2 + 10%×3) + 220 + 15 + 300 + 24 + 663]
     × (1 + 13% + 40%)                    ← kỹ năng 13% + sĩ khí 40% (nếu tính vào đây)
     + 1475 × 10%
   = 5887
```

> *Lưu ý: Tài liệu gốc gộp một số bonus vào các vị trí khác nhau. Kết quả cuối là 5887.*

---

### Ví dụ 2 — Dame cuối cùng của Hinata

**Thông tin thêm:**
- Kageyama toss cho Hinata: +973 [Tốc công] từ buff kỹ năng
- [KT tấn công]: 40% → Vùng_KT = 1.4
- Bội số kỹ năng: 389% → Vùng_SM = 3.89
- [Ý thức] = 149%, [Sức mạnh] = 249.5% → Vùng_BN = 3.495
- BNP: × 1 (đập bóng, không phải giao)
- Nhân đôi: × 2 (mặc định)

**Tính:**
```
Dame = (5887 + 973) × 1.4 × 3.89 × 3.495 × 2
     = 6860 × 1.4 × 3.89 × 3.495 × 2
     ≈ 261,000 (261k)
```

---

### Ví dụ 3 — Kiểm chứng thực tế (Hinata, 20 lần đập)

**Dữ liệu thực chiến:**
- 3 lần **không crit, nhân đôi ×2**: ~23.1k
- 7 lần **crit, nhân đôi ×1**: ~21.0k
- 10 lần **crit, nhân đôi ×2**: ~42.1k

**Tính lại từ đầu (Hinata cộng hưởng 14, Memory 5 sao):**

*Bước 1 — Vùng Chỉ số:*
```
CS = [1475 + 1475×(6.5%+0.3%+10%×2+15%×2) + 220+9+663+300+44+167] × 1.1
   = 4131.19
```
*(Ứng viên 167, kizuna trường +10% tính vào nhân 1.1 ở đây theo cách tính của tài liệu gốc)*

*Bước 2 — Các vùng còn lại:*
- Vùng_BN (không crit): × 1 | (crit): × (150% + 16.8% − 50%) = × 1.168...
  → Cụ thể: lực lượng Nice Play = 50% + 10% (tiềm năng) + 8.16% (phụ) = 68.16%
  → Không crit: × 1 | Crit: × (1 + 68.16%) = × 1.6816
- Vùng_KT: 1 + 10.2% + 2.04% = 1.1224
- Vùng_SM: không crit = ×2.5 | crit = ×(2.5 + 20%) = ×2.7
- BNP: × 1 | Nhân đôi: × 1 hoặc × 2

*Bước 3 — Tính dame:*
```
Không crit, ×2: 4131.19 × 1 × 1.1224 × 2.5 × 2 = 23,184 ≈ 23.1k ✓
Crit, ×2:       4131.19 × 1.6816 × 1.1224 × 2.7 × 2 = 42,105 ≈ 42.1k ✓
```

---

## V. LƯU Ý QUAN TRỌNG

1. **[Sức mạnh] và [Tinh thần] có giá trị gốc ẩn 50%** — không hiện trên panel nhưng luôn hoạt động.
2. **Ngọc (tiềm năng) % chỉ số chính** → thuộc Loại 1 (bonus chỉ số gốc) → nhân trước khi tính Loại 2.
3. **Ngọc % [KT tấn công/phòng thủ]** → thuộc Vùng Kỹ thuật, không phải Vùng Chỉ số.
4. **Ngọc % [Sức mạnh/Tinh thần]** → thuộc Vùng Bùng nổ.
5. **Kizuna trường học** có thể thuộc Loại 2 (% thông thường) hoặc Loại 3 (% × CS gốc) tùy từng kizuna cụ thể — cần phân biệt.
6. **Dame đập mạnh/tốc công thực chiến ổn định ở ×2** — khi tính toán lý thuyết dùng × 2 làm mặc định.

---

## VI. SO SÁNH NHANH — NGỌC NÀO MẠNH HƠN?

Với **[Đập mạnh] gốc = 5000**, cả 2 đều Nice Play:

| Trường hợp | Tính | Kết quả |
|---|---|---|
| Ngọc +35% [Đập mạnh] | 5000 × 1.35 = **6750** | 6750 × Vùng_BN × ... |
| Ngọc +40% [Sức mạnh] | 5000 × Vùng_BN(+40%) = 5000 × (1 + [Ý thức] × (0.5+0.4)) | Phụ thuộc [Ý thức] |

**Phân tích:**
- Ngọc [Đập mạnh] +35%: tăng **luôn luôn**, kể cả không Nice Play.
- Ngọc [Sức mạnh] +40%: tăng **chỉ khi Nice Play**.

Ngọc [Sức mạnh] vượt trội hơn khi: `[Ý thức] × 0.4 > 35%` → tức `[Ý thức] > 87.5%`.

> Với nhân vật có [Ý thức] cao (≥ ~90%), ngọc [Sức mạnh] thường mạnh hơn ngọc [Đập mạnh] cùng %.

---

## VII. NGUYÊN TẮC TỐI ƯU HÓA CHỈ SỐ

### 1. Hiệu suất giảm dần (Diminishing Returns)

Mỗi vùng nhân hoạt động độc lập. Khi một vùng đã tích lũy nhiều bonus, **giá trị cận biên của mỗi % thêm vào vùng đó sẽ giảm dần**.

**Công thức cận biên:** Thêm +1% vào vùng đang có X% tổng bonus → vùng đó tăng thêm:
```
1 / (100 + X) %
```

**Ví dụ so sánh:** Nên chọn [Chuyền bóng] hay [Kỹ thuật tấn công] ở ô phụ?

| Chỉ số | Vùng | X% hiện tại | Giá trị +10% tiếp theo |
|---|---|---|---|
| [Chuyền bóng] (L1 = 60%) | Vùng_CS | 60% | 10/160 = **6.25%** |
| [Kỹ thuật tấn công] (= 20%) | Vùng_KT | 20% | 10/120 = **8.33%** ✓ |
| [Chuyền bóng] (L1 = 100%) | Vùng_CS | 100% | 10/200 = **5.00%** |
| [Kỹ thuật tấn công] (= 50%) | Vùng_KT | 50% | 10/150 = **6.67%** ✓ |

**Quy tắc thực tế:**
- Nếu ô phụ đã nghiêng nặng về 1 chỉ số (VD: nhiều [Chuyền bóng]%), nên chọn chỉ số thuộc **vùng khác** (VD: [Kỹ thuật tấn công] thuộc Vùng_KT)
- Phân bổ đều qua các vùng nhân thường hiệu quả hơn dồn hết vào 1 vùng

---

### 2. Chỉ số hiếm > Chỉ số thường (Rare Stats > Normal Stats)

**Chỉ số hiếm:** [Ý thức], [Phản xạ], [Sức mạnh], [Tinh thần]

Những chỉ số này thuộc **Vùng Bùng nổ** — một vùng nhân riêng biệt, nhân lên TRÊN toàn bộ Vùng_CS. Vì vậy bất kỳ % cải thiện nào ở Vùng_BN đều khuếch đại toàn bộ chỉ số CS đã tích lũy.

#### Tại sao đặc biệt?

**Ví dụ:** Vùng_CS = 8000, Vùng_BN = 1.50, Vùng_KT = 1.30, Vùng_SM = 2.60

```
Dame gốc = 8000 × 1.50 × 1.30 × 2.60 = 40,560
```

Tăng Vùng_CS +10% (CS: 8000 → 8800):
```
Dame = 8800 × 1.50 × 1.30 × 2.60 = 44,616  (+10%)
```

Tăng Vùng_BN +10% (BN: 1.50 → 1.65):
```
Dame = 8000 × 1.65 × 1.30 × 2.60 = 44,616  (+10%)
```

→ **Cùng % tăng trên bất kỳ vùng nào đều cho kết quả như nhau** — điều khiến Rare Stats thực sự đặc biệt là:

1. **Vùng_BN có base ẩn 50%** ([Sức mạnh]/[Tinh thần]): Khi tích lũy còn thấp (gần 0%), mỗi % [Sức mạnh] được nhân với toàn bộ (50% base ẩn) → lợi tức cao ngay từ đầu
2. **[Ý thức]/[Phản xạ] ảnh hưởng xác suất Nice Play**: Tăng từ 50% → 100% gần gấp đôi tần suất kích hoạt Vùng_BN đầy đủ
3. **[Sức mạnh]/[Tinh thần] không có cap**: Khác với [Ý thức] bị giới hạn ở 100%, [Sức mạnh] luôn tiếp tục tăng dame

#### So sánh [Ý thức] vs [Sức mạnh] — cái nào ưu tiên trước?

Giá trị cận biên của từng chỉ số trong công thức kỳ vọng:
```
Vùng_BN_kỳ_vọng = 1 + (5% + [Ý thức]) × (50% + [Sức mạnh])
```

| | Giá trị cận biên của +1% |
|---|---|
| +1% [Ý thức] | × (50% + [Sức mạnh] tích lũy) |
| +1% [Sức mạnh] | × (5% + [Ý thức] tích lũy) |

**Kết luận:**
- **[Ý thức] > [Sức mạnh]** khi: `(50% + [Sức mạnh]) > (5% + [Ý thức])` → tức `[Ý thức] < [Sức mạnh] + 45%`
- Vì [Sức mạnh] có base ẩn 50% còn [Ý thức] chỉ có 5%, **[Ý thức] gần như luôn đáng ưu tiên hơn** cho đến khi [Ý thức] tích lũy vượt xa [Sức mạnh]
- Khi [Ý thức] đã đạt **cap 100%** → [Ý thức]/[Phản xạ] vô dụng, chỉ còn [Sức mạnh]/[Tinh thần] có giá trị trong Vùng_BN

> **Lưu ý:** Với kỹ năng **guaranteed Nice Play** (xác suất = 100%), [Ý thức]/[Phản xạ] hoàn toàn vô dụng cho lần kích hoạt đó — Vùng_BN khi đó chỉ phụ thuộc vào [Sức mạnh]/[Tinh thần].
