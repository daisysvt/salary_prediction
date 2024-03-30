import streamlit as st
from prediction_page import show_prediction_page
from analysis_page import show_analysis_page

st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/alicenkbaytop/",
        "Report a bug": "https://www.linkedin.com/in/alicenkbaytop/",
        "About": "# This is a salary prediction app based on survey!",
    },
)


def main():
    page = st.sidebar.radio("Go to", ("💵 Analysis", "💲 Prediction"))

    st.sidebar.warning(
        """
    :blue[Analysis and prediction have been processed based on the dataset derived from the survey results of the 'Önceki Yazılımcı'. 
    For more details, check out [here](https://oncekiyazilimci.medium.com/yaz%C4%B1l%C4%B1m-sekt%C3%B6r%C3%BC-maa%C5%9Flar%C4%B1-2024-e5d946e8e6da)].
    """
    )

    st.sidebar.write(
        "👨‍💻 [GitHub](https://github.com/alicenkbaytop/salary_prediction/blob/master)"
    )
    st.sidebar.write(
        "📊 [Kaggle](https://www.kaggle.com/code/alicenkbaytop/salary-prediction)"
    )
    st.sidebar.write("👨‍💼 [Linkedin](https://www.linkedin.com/in/alicenkbaytop/)")

    if page == "💵 Analysis":
        show_analysis_page()
    else:
        show_prediction_page()


if __name__ == "__main__":
    main()
