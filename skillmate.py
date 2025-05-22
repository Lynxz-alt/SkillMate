import streamlit as st

st.set_page_config(page_title="SkillMate - Marketplace Mahasiswa", layout="wide")

# Hero Section
st.markdown("""
    <div style="background-color:#f2f9ff; padding:3rem 1rem; border-radius:15px; text-align:center;">
        <h1 style="font-size: 3.5em; color:#4B8BBE; margin-bottom: 0.2em;">Selamat Datang di <span style="color:#FFA500;">SkillMate</span> 🎓</h1>
        <p style="font-size: 1.3em; color: #333;">Marketplace akademik bagi mahasiswa untuk <b>menjual</b> dan <b>mencari</b> jasa & skill: mentoring, desain, video editing, coding, dan kerajinan tangan.</p>
        <br>
        <a href='#daftar'><button style="background-color:#FFA500; color:white; font-size:1.2em; padding:0.7em 2em; border:none; border-radius:10px; cursor:pointer;">🚀 Gabung Sekarang</button></a>
    </div>
""", unsafe_allow_html=True)

st.markdown("### ")

# Fitur Unggulan
st.subheader("🧩 Fitur Unggulan SkillMate")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.markdown("### 🎓 Mentoring")
    st.caption("Dapatkan bimbingan akademik langsung dari teman mahasiswa.")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055646.png", width=80)
    st.markdown("### 🎨 Jasa Desain")
    st.caption("Poster, logo, hingga presentasi. Semuanya bisa kamu tawarkan!")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/427/427735.png", width=80)
    st.markdown("### 💻 Coding & Video Editing")
    st.caption("Kerjakan proyek bareng, edit video, atau bantu debug.")

st.markdown("---")

# Cara Kerja
st.markdown("## 🛠️ Cara Kerja SkillMate")
st.markdown("""
<ol style="font-size: 1.1em;">
<li><b>Daftar</b> sebagai penyedia atau pencari jasa</li>
<li><b>Jelajahi</b> jasa-jasa sesuai kebutuhan akademikmu</li>
<li><b>Hubungi</b> penyedia dan diskusikan pekerjaan</li>
<li><b>Transaksi</b> dengan sistem aman dan transparan</li>
<li><b>Ulas</b> pengalamanmu dan bantu pengguna lain</li>
</ol>
""", unsafe_allow_html=True)

# Testimoni
st.markdown("## ❤️ Apa Kata Pengguna?")
testi1, testi2 = st.columns(2)
with testi1:
    st.success("“Aku cari mentor Python buat UTS. Dapet di SkillMate, dan sekarang IPK-ku naik! 😭”\n\n– Amanda, TI 21")
with testi2:
    st.info("“Jasa desain yang aku tawarkan laris banget. Lumayan buat uang tambahan tiap bulan! 💸”\n\n– Rafi, DKV 22")

# CTA
st.markdown("### ")
st.markdown("""
<div id='daftar' style="background-color:#FFF3E0; padding:2rem 1rem; border-radius:10px; text-align:center;">
    <h2 style="color:#E65100;">Bergabung Sekarang dan Jadilah Bagian dari Revolusi Marketplace Mahasiswa!</h2>
    <p style="font-size: 1.2em;">Lebih dari <b>500+ mahasiswa</b> telah menawarkan dan menemukan jasa terbaik di kampus mereka.</p>
    <br>
    <a href='https://forms.gle/xyz'><button style="background-color:#E65100; color:white; font-size:1.1em; padding:0.7em 2em; border:none; border-radius:10px; cursor:pointer;">📩 Daftar Sekarang</button></a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<center><small>SkillMate © 2025 | Dibuat dengan ❤️ oleh Mahasiswa untuk Mahasiswa</small></center>", unsafe_allow_html=True)
