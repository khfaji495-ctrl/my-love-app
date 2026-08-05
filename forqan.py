import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="رسالة خاصة جداً", page_icon="❤️", layout="centered"
)

# تصميم وتنسيق CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #faf5f5;
    }
    h1 {
        color: #d9534f;
        text-align: center;
        font-family: 'Tahoma', sans-serif;
    }
    .love-text {
        font-size: 18px;
        color: #333333;
        text-align: center;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .message-box {
        font-size: 20px;
        color: #b30059;
        text-align: center;
        padding: 15px;
        background-color: #fff0f5;
        border-radius: 10px;
        border: 2px dashed #ffb6c1;
        margin-top: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# العنوان الرئيسي
st.markdown("<h1>إلى أغلى ما أملك ❤️</h1>", unsafe_allow_html=True)
st.write(
    "<p style='text-align: center; color: #666;'>تصميم خاص لعيونك وحدك</p>",
    unsafe_allow_html=True,
)

st.markdown("---")

# رسالة الصفا والترضية العامة
st.markdown(
    """
<div class="love-text">
<b>أحياناً العتب يكون بقدر الحب، وأنا ما عندي أغلى منكِ بهالدنيا.</b><br>
هذه الصفحة سويتها خصيصاً حتى أثبت لكِ أن زعلك ما يهون علي ابداً، وأن كل محاولة مني هي حتى تبقى ضحكتك منورة حياتي.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("### 🎮 فقرة التحدي والرضوة:")
st.write(
    "كل ما تجمعين قلب، راح تطلع لك رسالة خاصة من قلبي.. خلينا نشوف للنهاية:"
)

# قائمة العبارات
love_messages = [
    "لا تبقين زعلان من حبيبج زعلج يكسره",
    "يلا حبيبي ابتسم زعلك مو هين",
    "افدوا لهالابتسامه.",
    "احبج هواي ",
    "مالي غيرج بالدنيا ماريد يمرنا زعل",
]

# إدارة حالة النقاط في التطبيق
if "score" not in st.session_state:
    st.session_state.score = 0

st.write(f"🌟 عدد القلوب المجمعة: **{st.session_state.score} / 5**")

col1, col2 = st.columns(2)

with col1:
    if st.button("اضغطي هنا لجمع قلب 💖"):
        if st.session_state.score < len(love_messages):
            st.session_state.score += 1
            st.rerun()

with col2:
    if st.button("إعادة اللعبة 🔄"):
        st.session_state.score = 0
        st.rerun()

# عرض العبارة الخاصة بكل مرحلة بناءً على عدد القلوب التي جمعتها
if st.session_state.score > 0:
    current_msg = love_messages[st.session_state.score - 1]
    st.markdown(
        f'<div class="message-box">💖 {current_msg}</div>',
        unsafe_allow_html=True,
    )

# إذا جمعت كل القلوب (العدد 5)
if st.session_state.score >= len(love_messages):
    st.balloons()
    st.markdown(
        "<h3 style='color: #28a745; text-align: center; margin-top:20px;'>لقد"
        " جمعتِ كل قلبي، ولا زعل بعد اليوم! 🎉❤️</h3>",
        unsafe_allow_html=True,
    )

st.markdown("---")

# السؤال النهائي التفاعلي
st.write(
    "<h4 style='text-align: center;'>سامحتيني يبويه؟</h4>",
    unsafe_allow_html=True,
)

answer_col1, answer_col2 = st.columns(2)

with answer_col1:
    if st.button("نعم مسامحتك ❤️"):
        st.balloons()
        st.success(
            "يا بعد عمري، الله لا يحرمني من قلبك الطيب ولا يكتب زعل بيننا ابداً! ✨"
        )

with answer_col2:
    if st.button("لا بعدني زعلانة 😤"):
        st.warning(
            "ساعة 3 واني ما نايم ولا دجيجني نوم ما أكدر أنام واني عايفج ضايجة مني وكلبك ما راضي عني.\n\n"
            "فكرت هواي بغلطتي اني اعتذر الها وداعة ما كان قصدي أن أخليج تفهمين خطأ، الغلطة مني جنت بصدد الضحك والشقة وصارت هيك.\n\n"
            "جان المفروض انتبه لكلامي حتى لو جان شقة ومو قصد حتى ما أزعلج.\n\n"
            "لا أريد أكون وياج محاسب ولا أريد أكون بيوم من الأيام سبب كسرة بقلبك ولا أزعلج مني.\n\n"
            "كل اللي أريده أكون اني السند والرجال اللي تعتمدين عليه والحضن اللي يحويج ويشيل تعبج وهمج وما فد يوم أكون سبب بأذيتج.\n\n"
            "شيصير وشنو اللي تعاندين بيه راح تبقين حبيبتي وروحج هي روح حقج علي.\n\n"
            "من تكومين من نومتج سامحيني وتعاي ننسى الموضوع ووعد أول وأخري مرة أغلط وياج حتى لو جان بدون قصد مالي حيل لزعلج.\n\n"
            "انت كل دنيتي وأمير يضيع مو بس بلياج، حتى بزعلج اني أضيع! يلا اضغطي على الزر الأول 😉"
        )
