import re

class FormatStrings:

    def __init__(self):
        pass

    @staticmethod
    def merge_phones_like_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: FormatStrings.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.primary_home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.secondary_home_phone]))))

    @staticmethod
    def merge_emails_like_home_page(contact):
        return FormatStrings.clear_spaces("\n".join(
            filter(lambda x: x is not None and FormatStrings.clear(x) != "", [contact.email1, contact.email2, contact.email3])))

    @staticmethod
    def merge_contact_primary_phones_like_view_page(contact):
        return FormatStrings.merge_phones_like_view_page(contact.primary_home_phone, contact.mobile_phone, contact.work_phone)

    @staticmethod
    def merge_primary_info_like_view_page(contact):
        return " ".join(
            filter(lambda x: x is not None and x != "", [contact.first_name, contact.middle_name, contact.last_name]))

    @staticmethod
    def merge_phones_like_view_page(home, mobile, work):
        s = ""
        if (home is not None) and (FormatStrings.clear(home) is not ""):
            s = "H: %s\n" % home
        if (mobile is not None) and (FormatStrings.clear(mobile) is not ""):
            s = s + "M: %s\n" % mobile
        if (work is not None) and (FormatStrings.clear(work) is not ""):
            s = s + "W: %s\n" % work
        return s

    @staticmethod
    def clear(s):
        return re.sub("[- )(]", "", s)

    @staticmethod
    def clear_spaces(s):
        if s is None:
            return s
        else:
            return re.sub(" \n", "\n", re.sub(" +", " ", s)).rstrip().lstrip()

