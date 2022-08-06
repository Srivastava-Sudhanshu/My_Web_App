import logging
from .models import Fees,StudentFeeDetails
from My_Web_App.settings import DUE_EMAIL_TEMPLATE
import My_Web_App.send_mails as send_mails
from celery import shared_task

@shared_task()
def DueFeeNotification():
    try:
        logger = logging.getLogger('django')
        logger.info('Inside Task')
        student_fee_details = StudentFeeDetails.objects.all()
        for stud in student_fee_details:
            fees_details = Fees.objects.get(year = stud.student.current_year)
            stud.fees = fees_details.fee
            stud.due_amount = int(stud.fees) - int(stud.fees_paid)
            if stud.due_amount > 0:
                stud.name = stud.student.name
                stud.mailsubject = "Fees Due!"
                stud.email = stud.student.email
                stud.emailTemplate = DUE_EMAIL_TEMPLATE
                stud.purposeobject = stud.due_amount
                logger.info("Calling send mails for due")
                status = send_mails.SendMail(stud)
    except Exception as e:
        logger.info(f"Error: {e}")
        status = "Something went wrong!!"
        
    return status