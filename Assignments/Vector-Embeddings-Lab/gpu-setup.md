## 1. Make sure GPU is available (PyTorch + CUDA installed)

Run this in Python:

```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
```

### Expected:

* `True`
* `"NVIDIA …"`

If it prints `False`, you are not using a CUDA build of PyTorch.


# ⭐ Step 3 — Install the stable NVIDIA drivers

**Do NOT install 545** — it’s failing on your kernel (6.8).

Install 535 instead:

```bash
sudo apt install nvidia-driver-535 nvidia-dkms-535 nvidia-utils-535
```

---

# 🔄 Step 4 — Reboot

```bash
sudo reboot
```

---

# 🧪 Step 5 — Verify driver

After reboot:

```bash
nvidia-smi
```

Expected output:

```
NVIDIA-SMI 535.xx.xx   Driver Version: 535.xx.xx   CUDA Version: 12.x
GPU Name: Quadro T1000 Mobile
```

---

# ☣️ If 535 also fails (unlikely)

Then we install the **server variant**, which is more compatible:

```bash
sudo apt install nvidia-driver-535-server
```

---

# 🧠 Why 545 fails

* Ubuntu 22.04 + kernel 6.8 often has DKMS problems with 545
* 535 is the **recommended long-term stable** driver for Turing GPUs (TU117)

---

# 🚀 After GPU works, install CUDA PyTorch

```bash
pip uninstall torch -y
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

Test in Python:

```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

---

## 🔥 Before we continue — I need this from you:

Please run the following and paste output **if 535 fails**:

```bash
cat /var/lib/dkms/nvidia/545.29.06/build/make.log | tail -n 30
```

…but let’s try the stable driver first — **99% chance it will fix your problem.**
